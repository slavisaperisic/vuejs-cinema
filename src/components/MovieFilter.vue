<template>
    <div id="movie-filter">
        <h2>Filter Results</h2>
        <div class="filter-group">
            <check-filter v-for="genre in genres" v-bind:genreTitle="genre" v-on:check-filter="checkFilter"></check-filter>
        </div>
    </div>
</template>

<script>
    import genres from "../util/genres";
    import CheckFilter from "../components/CheckFilter.vue";

    export default {
        methods: {
            checkFilter(category, title, checked) {
                this.$emit('check-filter', category, title, checked);
            }
        },
        data() {
            return {
                genres
            }
        },
        components: {
            CheckFilter
        }
    }
</script>