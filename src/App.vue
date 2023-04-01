<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-toolbar-title>Minhas Receitas</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="white" @click="showNewRecipeModal">Nova Receita</v-btn>
    </v-app-bar>
    <recipe-list :recipes="recipes"></recipe-list>
    <v-dialog v-model="showNewRecipe" width="500">
      <v-card>
        <v-card-title>Nova Receita</v-card-title>
        <v-card-text>
          <v-text-field v-model="newRecipe.title" label="Título"></v-text-field>
          <v-textarea v-model="newRecipe.ingredients" label="Ingredientes"></v-textarea>
          <v-textarea v-model="newRecipe.directions" label="Modo de Preparo"></v-textarea>
          <v-textarea v-model="newRecipe.notes" label="Observações"></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="saveNewRecipe">Salvar</v-btn>
          <v-btn @click="closeNewRecipeModal">Cancelar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-app>
</template>

<script>

import RecipeList from './components/RecipeList.vue';
import {fetchRecipes, createRecipe} from './services/recipes.js';

export default {
  components: {
    RecipeList,
  },
  async created(){
    this.fetchRecipes()
    
  },
  data() {
    return {
      recipes: [],
      showNewRecipe: false,
      newRecipe: {
        title: '',
        ingredients: '',
        directions: '',
        notes: ''
      }
    };
  },
  methods: {
    fetchRecipes(){

      fetchRecipes().then((response) => {
        console.log(response.data)
        this.recipes = response.data
      })
      .catch(function (error) {
          console.log(error);
      });
    },
    createRecipe(recipe){
      createRecipe(recipe).then((response) => {
        console.log(response)
        this.fetchRecipes()
      }).catch(function (error) {
          console.log(error);
      });
    },
    saveNewRecipe() {
      const newRecipe = {
        id: this.recipes.length + 1,
        title: this.newRecipe.title,
        ingredients: this.newRecipe.ingredients,
        directions: this.newRecipe.directions,
        notes: this.newRecipe.notes,
        image: "https://www.example.com/default-image.jpg"
      };
      createRecipe(newRecipe)
      // this.recipes.push(newRecipe);
      this.closeNewRecipeModal();
    },
    closeNewRecipeModal() {
      this.showNewRecipe = false;
      this.newRecipe.title = '';
      this.newRecipe.ingredients = '';
      this.newRecipe.directions = '';
      this.newRecipe.notes = '';
    },
    showNewRecipeModal() {
      this.showNewRecipe = true;
    }
  }
}
</script>
