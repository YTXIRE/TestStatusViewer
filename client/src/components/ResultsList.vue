<template>
	<el-form :inline="true">
		<el-form-item label="Проект" class="form">
			<el-select v-model="project" placeholder="Выберите проект" size="large" class="form">
				<el-option
					v-for="item in projects"
					:key="item"
					:label="item"
					:value="item"
				/>
			</el-select>
		</el-form-item>
	</el-form>
	<div v-for="report in reports_list" :key="report.id">
		<ReportItem :report="report" @changeAccordion="changeAccordion"/>
	</div>
	<div v-if="reports_list.length === 0">
		<el-card shadow="always">
			Нет данных
		</el-card>
	</div>
</template>

<script>
import axios from 'axios';
import {API_ULR} from "../config.json"
import ReportItem from "@/components/ReportItem.vue";

export default {
	components: {ReportItem},
	data() {
		return {
			reports_list: [],
			projects: [],
			project: ''
		}
	},
	methods: {
		changeAccordion(id) {
			this.reports_list.map(report => {
				if (report.id === id) {
					report.show = !report.show
				}
			})
		},
		async fetch_data() {
			const data = await axios.get(`${API_ULR}/get_logs?project=${this.project}`);
			let result = [];
			data.data.data.map(report => {
				result.push({
					...report,
					show: this.checkShow(report.id, this.reports_list.filter(report => report.show)),
					created_at: new Date(report.created_at * 1000).toLocaleString(),
				})
			});
			this.reports_list = result;
		},
		checkShow(id, shows_list) {
			return shows_list.filter(report => report.id === id)[0]?.show
		},
		async get_projects() {
			const data = await axios.get(`${API_ULR}/get_projects`);
			this.projects = data.data.data
			this.project = this.projects[0]
		}
	},
	async mounted() {
		await this.get_projects();
		setInterval(async () => {
			await this.fetch_data();
		}, 2000)
	},
	watch: {
		project: async function () {
			if (this.project !== '') {
				await this.fetch_data();
			}
		},
	}
}
</script>

<style scoped>
.form {
	width: 100% !important;
}
</style>