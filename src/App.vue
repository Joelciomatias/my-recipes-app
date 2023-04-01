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

export default {
  components: {
    RecipeList,
  },
  data() {
    return {
      recipes: [
        {
          id: 1,
          title: "Macarrão com queijo",
          ingredients: "macarrão, queijo, leite, manteiga",
          directions: "Cozinhe o macarrão, misture com o queijo derretido, adicione o leite e a manteiga e misture tudo",
          notes: "Rápido e fácil de fazer",
          image: "https://www.example.com/mac-cheese.jpg"
        },
        {
          id: 2,
          title: "Bolo de cenoura",
          ingredients: "cenoura, açúcar, farinha, óleo, ovos",
          directions: "Bata os ovos, misture com os outros ingredientes, asse em uma forma",
          notes: "Delicioso com cobertura de cream cheese",
          image: "https://www.example.com/carrot-cake.jpg"
        }
      ],
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
    saveNewRecipe() {
      const newRecipe = {
        id: this.recipes.length + 1,
        title: this.newRecipe.title,
        ingredients: this.newRecipe.ingredients,
        directions: this.newRecipe.directions,
        notes: this.newRecipe.notes,
        image: "https://www.example.com/default-image.jpg"
      };
      this.recipes.push(newRecipe);
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
