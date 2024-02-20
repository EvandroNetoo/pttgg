<script setup>
import AnimatedPlaceholder from '@/components/AnimatedPlaceholder.vue'
</script>

<template>
    <div class="profile-header" style="min-height: 160px;">
        <main>
            <AnimatedPlaceholder style="margin-right: 40px;" height="100px" width="100px" borderRadius="20px" />
            <div>
                <p style="padding: 5px  0;">
                    <AnimatedPlaceholder height="30px" width="200px" borderRadius="3px" />
                </p>
                <p style="padding: 5px  0;">
                    <AnimatedPlaceholder height="10px" width="120px" borderRadius="3px" />
                </p>

                <button class="update-button">Update</button>
            </div>
        </main>
    </div>
</template>

<script>
export default {

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