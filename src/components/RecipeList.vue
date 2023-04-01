<template>
  <v-container>
    <v-row>
      <v-col v-for="recipe in recipes" :key="recipe.id" cols="12" md="6" lg="4">
        <v-card>
          <v-img :src="recipe.image" height="200px"></v-img>
          <v-card-title>{{ recipe.title }}</v-card-title>
          <v-card-text>{{ recipe.ingredients }}</v-card-text>
          <v-card-text>{{ recipe.directions }}</v-card-text>
          <v-card-text>{{ recipe.notes }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['recipes']
}
</script>
