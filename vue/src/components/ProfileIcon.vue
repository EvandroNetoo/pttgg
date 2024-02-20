<script setup>
const props = defineProps(['profileIconUrl', 'level'])
</script>

<template>
    <div class="profile-icon">
        <Transition>
            <div v-if="profileIconUrl" key="profile">
                <img class="profile-image" :src="profileIconUrl" alt="Profile Icon">
                <div class="div-profile-level">
                    <span class="profile-level">{{ level }}</span>
                </div>
            </div>
        </Transition>

        <div v-if="profileIconUrl === null" class="skeleton"></div>
    </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>

.skeleton {
    height: 100px;
    width: 100px;
    background-color: var(--skeleton-color);
    border-radius: 20px;
}

.profile-icon {
    position: relative;
    display: block;
    flex-basis: 100px;
    height: 100px;
    width: 100px;
    margin-right: 40px;
}

.profile-image {
    display: inline;
    height: 100px;
    width: 100px;
    border-radius: 20px;
    overflow-y: clip;
    overflow-x: clip;
}

.div-profile-level {
    display: block;
    height: 20px;
    margin-top: -20px;
    text-align: center;
}

.profile-level {
    background-color: black;
    color: white;
    display: inline-block;
    font-size: 12px;
    line-height: 20px;
    border-radius: 10px;
    padding: 0px 8px 0px 8px;
}
</style>