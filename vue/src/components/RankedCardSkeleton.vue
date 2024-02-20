<script setup>
import AnimatedPlaceholder from '@/components/AnimatedPlaceholder.vue'

const props = defineProps(['rankedInfos', 'rankedName'])
</script>

<template>
    <div class="card">
        <div class="title">
            <p style="font-weight: bold;">{{ rankedName }}</p>
        </div>
        <div class="body">
            <AnimatedPlaceholder height="70px" width="93px" border-radius="50%"/>
            <div class="" style="position: relative; display: flex; justify-content: space-between; width: 100%; margin-left: 10px;">
                <div  style="position: relative;">
                    <AnimatedPlaceholder style="margin-bottom: 5px;" height="20px" width="80px" border-radius="3px"/>
                    
                    <AnimatedPlaceholder height="12px" width="30px" border-radius="3px"/>
                </div>

                <div style="display: flex; align-items: center;">
                    <div style="display: flex; flex-direction: column; align-items: end;">
                        <AnimatedPlaceholder style="margin-bottom: 5px;" height="12px" width="60px" border-radius="3px"/>

                        <AnimatedPlaceholder style="margin-bottom: 5px;" height="12px" width="80px" border-radius="3px"/>
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
</style>