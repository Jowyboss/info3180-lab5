<script setup>
    import { ref, onMounted } from 'vue';
    
    let csrf_token = ref(""); 
    let isError = ref()
    let response = ref({})

    function getCsrfToken(){
        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
    }


    onMounted(() => {
        getCsrfToken()
    });

    function saveMovie(){
        

        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);


        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken':csrf_token.value
            }
            
        })

            .then(function (response) {
                return response.json();
            })

            .then(function (data) {
            
                console.log(data);
                

                data.hasOwnProperty('errors') ? 
                isError.value = true
                : isError.value = false

                response.value = data
                
            })

            .catch(function (error) {
                console.log(error);
            });
    }
</script>


<template>

    <h1>Movie Form</h1>

    <div v-if="isError == false && response.message != '' " class="successful">{{ response.message }}</div>
    
    <div v-if="isError == true" class="">
        <ul class="errors">
            <li v-for="error in response.errors" >
                {{ error }}
            </li>
        </ul>
    </div>

    <form id="movieForm" class="form-group mb-3" @submit.prevent="saveMovie" enctype="multipart/form-data">
        <div>
            <label for="title" class="form-label">Movie Title:</label>
            <input type="text" name="title" class="form-control">
        </div>

        <div>
            <label for="description" class="form-label">Movie Description:</label>
            <textarea name="description" class="form-control"></textarea>
        </div>

        <div>
            <label for="poster" class="form-label">Movie Poster:</label>
            <input type="file" name="poster" class="form-control" accept=".jpg,.png,.jpeg">
        </div>

        <button class="btn btn-primary" type="submit">Save Movie</button>
    </form>
</template>


<style>
/* Add any component specific styles here */
form{
    background-color: white;
    padding: 2rem;
    border-radius: 10px;
}

form > div{
    margin-bottom: 40px;
}

button{
    border: none !important;
}

button:hover{
    background-color: rgb(19, 195, 16) !important;
}

.form-label{
    font-weight: 700;
}

.errors{
    list-style-type: none;
    display: flex;
    justify-content: center;
    gap: 10px;
}

.errors > li{
    border: 2px dashed rgb(237, 92, 92);
    background-color: rgb(239, 179, 179);
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
}

.successful{
    border: 2px dashed rgb(4, 224, 30);
    background-color: rgb(179, 238, 174); 
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
}



</style>