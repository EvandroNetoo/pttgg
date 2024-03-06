<script setup>
import ProfileIcon from '@/components/ProfileIcon.vue';

const props = defineProps(['summonerData'])
</script>

<template>
    <div class="profile-header">
        <main>
            <ProfileIcon :profileIconUrl="summonerData.icon_url" :level="summonerData.level" />
            <div>
                <p style="font-size: 30px;">
                    <span>{{ summonerData.game_name }} </span>
                    <span style="opacity: 70%;">#{{ summonerData.tag_line }}</span>
                </p>

                <p v-if="summonerData.name != ''">Prev: {{ summonerData.name }}</p>

                <button @click="$emit('updateSummoner')" class="update-button">Update</button>
            </div>
        </main>
    </div>
</template>

<script>
export default {
    methods: {
    }
}
</script>

<style lang="css" scoped>
.profile-header {
    display: flex;
    justify-content: center;
    background-color: var(--color-border);
    min-width: 1080px;
}

main {
    min-width: 1080px;
    padding: 20px 0;
    display: flex;
    align-items: center;
}

.update-button {
    background-color: transparent;
    border: hsla(160, 100%, 37%, 1) 3px solid;
    border-radius: 10px;
    padding: 10px 15px;
    color: var(--color-text);
    font-weight: bold;
    margin-top: 5px;
    transition: .2s;
}

.update-button:hover {
    border: white 3px solid;
    background-color: hsla(160, 100%, 37%, 1);
    color: white;
}

.update-button:active {
    background-color: hsla(160, 100%, 37%, .7);
}
</style>