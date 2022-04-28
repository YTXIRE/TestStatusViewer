<template>
	<el-card :class="report.status" shadow="hover" @click="$emit('changeAccordion', report.id)">
		<div class="title">
			<span class="test_name">{{ report.test_name }}</span>
			<span class="created_at">{{ report.created_at }}</span>
		</div>
	</el-card>
	<el-row v-if="report.show" class="message" :gutter="12">
		<el-col :span="24">
			<el-card shadow="always">
					<pre v-if="report.message" class="message_text">
						{{report.message}}
					</pre>
				<div v-else>
					Не парься! Все ок!
				</div>
			</el-card>
		</el-col>
	</el-row>
</template>

<script>
export default {
	props: {
		report: {
			type: Object,
			require: true
		}
	},
	name: "ReportItem",
	emits: ['changeAccordion']
}
</script>

<style scoped>
.failed {
	background: #F56C6C;
	margin-bottom: 5px;
}

.passed {
	background: #67C23A;
	margin-bottom: 5px;
}

.title {
	width: 100%;
	height: 30px;
	color: #fff;
	font-size: 20px;
	/*margin-bottom: 5px;*/
	display: flex;
}

.title:hover {
	cursor: pointer;
}

.test_name {
	display: block;
	padding-top: 2px;
	text-align: left;
	width: 50%;
}

.created_at {
	display: block;
	width: 50%;
	text-align: right;
	padding-top: 4px;
}

.message {
	margin-top: 10px;
	margin-bottom: 15px;
}

.message_text {
	text-align: left !important;
	margin-left: 0 !important;
	overflow: auto;
}
</style>