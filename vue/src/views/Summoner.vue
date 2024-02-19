<script setup>
import TheHeader from '@/components/TheHeader.vue';
import ProfileIcon from '@/components/ProfileIcon.vue';
</script>

<template>
	<TheHeader class="the-header" />

	<div class="container">
		<main>
			<ProfileIcon />
		</main>
	</div>
</template>

<style>
.container {
	display: flex;
	justify-content: center;
}

.the-header {
	margin-bottom: 20px;
}

main {
	min-width: 1080px;
}
</style>

<script>
export default {
	data() {
		return {
			summonerData: null,
			rankedSoloDuo: null,
			rankedFlex: null,
		}
	},
	created() {
		fetch('http://127.0.0.1:8000/api/summoners/br/ptt-bella')
			.then(response => {
				if (!response.ok) {
					throw new Error('Falha ao buscar dados da API');
				}
				return response.json();
			})
			.then((data) => {
				this.summonerData = data.summoner;
				this.rankedSoloDuo = data.ranked_solo_duo;
				this.rankedFlex = data.ranked_flex;
				console.log(data)
			})
			.catch(error => {
				console.error('Erro na chamada da API:', error);
			});
	}
}
</script>

<style></style>
