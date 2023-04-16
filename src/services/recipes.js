const axios = require('axios');
const url = 'http://127.0.0.1:5000'

export async function fetchRecipes(){
    return await axios.get(url + '/recipes')
}

export async function createRecipe(data){
    return await axios.post(url + '/recipes', data)
}