<script setup>
import AnimatedPlaceholder from './AnimatedPlaceholder.vue'

const props = defineProps(['rankedInfos', 'rankedName'])
</script>

<template>
    <div class="card">
        <div class="title">
            <p style="font-weight: bold;">{{ rankedName }}</p>
        </div>
        <div class="body">
            <img height="70px" width="70px" :src="`/ranked_emblems/${rankedInfos.tier}.png`">
            <div style="display: flex; justify-content: space-between; width: 100%; margin-left: 10px;">
                <div>
                    <p>
                        {{ rankedInfos.tier }}
                        <span v-if="!['MASTER', 'GRANDMASTER', 'CHALLENGER'].includes(rankedInfos.tier)">
                            {{ rankedInfos.rank }}
                        </span>
                    </p>

                    <p style="font-size: small;" class="m-0">{{ rankedInfos.pdls }} LP</p>
                </div>

                <div style="display: flex; align-items: center;">
                    <div style="display: flex; flex-direction: column; align-items: end;">
                        <p style="font-size: small;">
                            {{ rankedInfos.wins }}W {{ rankedInfos.losses }}L
                        </p>

                        <p style="font-size: small;">
                            Win Rate {{ rankedInfos.win_rate }}%
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
.card {
    border-radius: 5px;
    background-color: var(--color-border);
    border: var(--color-border-hover) 1px solid;
}

.title {
    padding: 5px;
    border-bottom: var(--color-border-hover) 1px solid;
}

.body {
    padding: 5px;
    display: flex;
    align-items: center;
}

img {
    background-color: var(--color-border-hover);
    border-radius: 35px;
}
</style>