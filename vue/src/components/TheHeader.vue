<script>
</script>

<template>
    <header>
        <div class="header-container">
            <img width="40px" src="/ptt-icon.png" alt="">
            <div class="search-container">
                <select name="region">
                    <option v-for="region in regions" value="{{ region }}">{{ region }}</option>
                </select>
                <div class="input-container">
                    <input type="text" v-model="nameTagInput">
                    <p v-show="this.nameTagInput === ''" class="placeholder">
                        <span class="span-placeholder">Game Name </span>
                        <span class="span-placeholder tag-placeholder">#{{ selectRegion }}1
                        </span>
                    </p>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    data() {
        return {
            nameTagInput: '',
            selectRegion: 'BR',
            regions: [
                'BR',
                'EUN',
                'EUW',
                'JP',
                'KR',
                'LAN',
                'LAS',
                'NA',
                'OC',
                'TR',
                'RU',
                'PH',
                'SG',
                'TH',
                'TW',
                'VN',
            ]
        };
    },
}
</script>

<style lang="css" scoped>
header {
    position: relative;
    left: 0;
    top: 0;
    width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 1080px;
    border-bottom: var(--color-border-hover) solid 1px;
}


.header-container {
    display: flex;
    align-items: center;
    min-width: 1080px;
    height: 100%;
    padding: 10px 0;
}

.search-container {
    width: 100%;
    height: 40px;
    margin-left: 10px;
    background-color: var(--vt-c-white-mute);
    border-radius: 5px;
    display: flex;
    align-items: center;
}



select {
    height: 100%;
    background-color: transparent;
    border: 0;
}

select:focus {
    outline: 0;
}

.input-container {
    width: 100%;
    height: 100%;
    position: relative;
    display: flex;
    align-items: center;
    margin-left: 5px;
}

input {
    width: 100%;
    height: 100%;
    border: 0;
    border-radius: 5px;
    background-color: transparent;
    padding: 0;
}

input:focus {
    outline: 0;
}

.placeholder {
    pointer-events: none;
    position: absolute;
    left: 0;
    margin-left: 1px;
    color: rgba(55, 55, 55, 0.882);
}

.span-placeholder {
    opacity: 0.6;
}

.tag-placeholder {
    background-color: rgba(94, 94, 94, .2);
    border-radius: 3px;
    padding: 2px;
}
</style>