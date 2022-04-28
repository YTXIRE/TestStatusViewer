<template>
	<h1>Test Result Viewer</h1>
	<div class="container">
		<ResultsList/>
	</div>
</template>

<script>
import ResultsList from "@/components/ResultsList.vue";

export default {
	components: {ResultsList}
}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	width: 1000px !important;
	margin: 10px auto;
}

.el-form-item__label {
	margin-top: 5px !important;
}
</style>
