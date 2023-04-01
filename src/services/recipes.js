import axios from 'axios';

export async function fetchRecipes(){
    const response = await axios.get('http://localhost:5000/recipes')
    return response
}

export async function createRecipe(recipe){
    const response = await axios.post('http://localhost:5000/recipes', recipe)
    return response
}