<template>
    <div v-bind:class="{'check-filter' : true, 'active' : checked}" @click="checkFilter">
        <span class="checkbox"></span>
        <span class="check-filter-title">{{genreTitle}}</span>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                checked: false
            }
        },
        props: ['genreTitle'],
        methods: {
            checkFilter() {
                this.checked = !this.checked;
                this.$emit('check-filter', 'genre', this.genreTitle, this.checked);
            }
        }
    }
</script>