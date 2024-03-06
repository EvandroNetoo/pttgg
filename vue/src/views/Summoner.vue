<script setup>
import TheHeader from '@/components/TheHeader.vue';
import ProfileHeader from '@/components/ProfileHeader.vue';
import ProfileHeaderSkeleton from '@/components/ProfileHeaderSkeleton.vue';
import RankedCard from '@/components/RankedCard.vue';
import RankedCardSkeleton from '@/components/RankedCardSkeleton.vue';
import Match from '@/components/Match.vue';
</script>

<template>
	<TheHeader class="the-header" />
	<div v-if="!error404">
		<ProfileHeader v-if="!loading" @update-summoner="funcUpdateSummoner" class="profile-header"
			:summonerData="summonerData" />
		<ProfileHeaderSkeleton v-else class="profile-header" />

		<div class="container">
			<main>
				<div v-if="!loading" style="min-width: 332px; display: flex; flex-direction: column; gap: 10px">
					<RankedCard rankedName="Ranked Solo" :rankedInfos="rankedSoloDuo"></RankedCard>
					<RankedCard rankedName="Ranked Flex" :rankedInfos="rankedFlex"></RankedCard>
				</div>
				<div v-else style="min-width: 332px; display: flex; flex-direction: column; gap: 10px">
					<RankedCardSkeleton rankedName="Ranked Solo"></RankedCardSkeleton>
					<RankedCardSkeleton rankedName="Ranked Flex"></RankedCardSkeleton>
				</div>

				<div class="matches">
					<Match v-for="matchData in mathcesData" :matchData="matchData"/>
				</div>


			</main>
		</div>
	</div>
	<div v-else>
		<p style="font-size: 30px; font-weight: bold; text-align: center;">Results not found.</p>
	</div>
</template>

<style scoped>
.container {
	display: flex;
	justify-content: center;
	min-width: 1080px;
}

main {
	min-width: 1080px;
	display: flex;
	gap: 10px
}

.the-header {
	margin-bottom: 10px;
}

.profile-header {
	margin-bottom: 10px;
}

.matches {
	display: flex;
	flex-direction: column;
	width: 100%;
	gap: 10px;
}
</style>

<script>
export default {
	data() {
		return {
			summonerData: {
				game_name: null,
				tag_line: null,
				name: null,
				profile_icon_id: null,
				level: null,
				icon_url: null,
			},
			rankedSoloDuo: {
				tier: null,
				rank: null,
				pdls: null,
				wins: null,
				losses: null,
				win_rate: null,
				ranked_emblem: null,
			},
			rankedFlex: {
				tier: null,
				rank: null,
				pdls: null,
				wins: null,
				losses: null,
				win_rate: null,
				ranked_emblem: null,
			},
			mathcesData: null,
			loading: true,
			error404: false,

		}
	},
	mounted() {
		fetch(`http://127.0.0.1:8000/api/summoners/${this.$route.params.region}/${this.$route.params.gameNameTagLine}`)
			.then(response => {
				if (response.status == 404) {
					this.error404 = true
				}
				else if (!response.ok) {
					throw new Error('Falha ao buscar dados da API');
				}
				return response.json();
			})
			.then((data) => {
				this.summonerData = data.summoner
				this.rankedSoloDuo = data.ranked_solo_duo
				this.rankedFlex = data.ranked_flex
				this.mathcesData = data.matches
				this.loading = false
				console.log(data)
			})
			.catch(error => {
				console.error('Erro na chamada da API:', error);
			});
	},
	methods: {
		funcUpdateSummoner() {
			console.log('updating summoner')
			fetch(`http://127.0.0.1:8000/api/summoners/${this.$route.params.region}/${this.$route.params.gameNameTagLine}/update/`)
				.then(response => {
					if (response.status == 404) {
						this.error404 = true
					}
					else if (!response.ok) {
						throw new Error('Falha ao buscar dados da API');
					}
					return response.json();
				})
				.then((data) => {
					this.summonerData = data.summoner;
					this.rankedSoloDuo = data.ranked_solo_duo;
					this.rankedFlex = data.ranked_flex;
					this.loading = false
				})
				.catch(error => {
					console.error('Erro na chamada da API:', error);
				});
		},
	}

}
</script>

<style></style>
