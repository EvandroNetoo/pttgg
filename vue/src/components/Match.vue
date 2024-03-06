<script setup>
const props = defineProps(['matchData'])
</script>

<template>
    <div class="match">
        <div>
            <p class="small-font">{{ removeFirstAndLastWord(matchData.queue_type) }}</p>
            <p class="small-font">{{ matchTimeAgo }} ago</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            matchTimeAgo: ''

        }
    },
    created() {
        this.updateMatchtimegap()
        setInterval(this.updateMatchtimegap, 60 * 1000)
    },
    methods: {
        removeFirstAndLastWord(sentence) {
            let words = sentence.split(" ");

            words.shift();

            words.pop();

            let newsentence = words.join(" ");

            return newsentence;
        },
        updateMatchtimegap() {
            const dateUTC = new Date(this.matchData.end_at)
            let nowUTC = new Date()
            const gapInMilissegundos = nowUTC - dateUTC
            const gapInminutes = gapInMilissegundos / 1000 / 60

            const days = parseInt(gapInminutes / 60 / 24)
            const hours = parseInt(gapInminutes / 60 - days * 24)
            const minutes = parseInt(gapInminutes - hours * 60 - days * 60 * 24)

            if (days > 0) {
                this.matchTimeAgo = `${days}d ${hours}h`;
            } else if (hours > 0 ) {
                this.matchTimeAgo = `${hours}h  ${minutes}m`;
            }else {
                this.matchTimeAgo = `${minutes}m`;
            }

        }
    }
}
</script>

<style lang="css" scoped>
.small-font {
    font-size: 11px;
}

.match {
    display: flex;
    align-items: center;
    border-radius: 3px;
    background-color: var(--color-border);
    border: var(--color-border-hover) 1px solid;
    padding: 5px;
}
</style>