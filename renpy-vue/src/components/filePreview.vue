<template>
	<div class="newUpload">
		<component :is="tag" class="file-preview">
			<img :src="file.url" :alt="file.file.name" :title="file.file.name" />
			<span class="status-indicator loading-indicator" v-show="file.status == 'loading'">In Progress</span>
			<span class="status-indicator success-indicator" v-show="file.status == true">Uploaded</span>
			<span class="status-indicator failure-indicator" v-show="file.status == false">Error</span>
		</component>
		<span>Name</span>
		<input type="text" class="name" v-model="fileName" @change="$emit('editFileName', file, fileName)">
		<span>Type</span>
		<select v-model="fileType" @change="$emit('editFileType', file, fileType)">
			<option value="character">Character</option>
			<option value="background">Background</option>
			<option value="sfx">Sound Effect</option>
			<option value="music">Music</option>
		</select>
		<button @click="$emit('remove', file)" class="close-icon" aria-label="Remove">×</button>
	</div>
</template>

<script>
export default {
    name: 'filePreview',
    props: {
        file: { type: Object, required: true },
        tag: { type: String, default: 'li' },
    },
    emits: ['remove', 'editFileType', 'editFileName'],
	data() {
		return{
			fileType: String,
			fileName: String
		}
	},
	mounted() {
		this.fileName = this.file.file.name.split(".")[0].replace(/[^a-zA-Z0-9 -]/g, '')
		this.fileType = "character"
	}
}
</script>

<style scoped lang="scss">
.newUpload {
	width: 98%;
	height: 30%;
	background: #6c6;
	border-radius: 11px;
	margin-bottom: 1%;
	padding: 1%;
    order: 0;
    flex-grow: 0;
	display: flex;
	flex-direction: row;
	align-items: center;
}
.close-icon {
	--size: 20px;
	position: relative;
	right:0%;
	top:0%;
	line-height: var(--size);
	height: var(--size);
	border-radius: var(--size);
	box-shadow: 0 0 5px currentColor;
	appearance: none;
	border: 0;
	padding: 0;
	width: var(--size);
	font-size: var(--size);
	background: #933;
	color: #fff;
	cursor: pointer;
}
.file-preview {
	height: 100%;
	margin: 1% 2.5%;
	position: relative;
	border: solid 2px #000;
	border-radius: 11px;
	background-color: #fff;
	aspect-ratio: 1/1;
	overflow: hidden;
	img {
		width: 100%;
		height: 100%;
		display: block;
		object-fit: scale-down;
	}
	.status-indicator {
		--size: 20px;
		position: absolute;
		line-height: var(--size);
		height: var(--size);
		border-radius: var(--size);
		box-shadow: 0 0 5px currentColor;
		right: 0.25rem;
		appearance: none;
		border: 0;
		padding: 0;
	}
	.status-indicator {
		font-size: calc(0.75 * var(--size));
		bottom: 0.25rem;
		padding: 0 10px;
	}
	.loading-indicator {
		animation: pulse 1.5s linear 0s infinite;
		color: #000;
	}
	.success-indicator {
		background: #6c6;
		color: #040;
	}
	.failure-indicator {
		background: #933;
		color: #fff;
	}
}
</style>