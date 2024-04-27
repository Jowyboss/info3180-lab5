<script setup>
    import { ref, onMounted } from "vue";
    let movies = ref([]); 

    onMounted(() => {
        fetchMovies();
    })

    function fetchMovies(){
        fetch("/api/v1/movies", {
                method: 'GET',
                
                
        })

                .then(function (response) {
                    return response.json();
                })

                .then(function (data) {
                
                    console.log(data);
                    

                    movies.value = data.movies;
                })

                .catch(function (error) {
                    console.log(error);
                });
    }

</script>

<template>
    <h1>Movies</h1>


    <div class="list">

        <div v-for="movie in movies" class="movie">
            <div class="thumbnail">
                <img :src="movie.poster" :alt="movie.title + ' poster'" />
            </div>

            <div class="info">
                <h4>{{movie.title}}</h4>
                <p>{{movie.description}}</p>
            </div>
            
        
        </div>

    </div>
</template>

<style>

.list{
    display: grid;
    grid-template-columns: repeat(2, 1fr); 
    grid-gap: 30px; 
    grid-auto-rows: 300px;
}

.movie{
    background-color: #fff;
    overflow: hidden;
    border-radius: 10px;
    position: relative;
    max-height: 300px;
    display: flex;
    border: 1px solid #e1e1e1;
}

.thumbnail {
    width: 100%;
    overflow: hidden;
}

.thumbnail img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;

}

.info{
    padding: 1rem;
    max-width: 400px;
    word-wrap: break-word;

    overflow-y: auto;
}

</style>