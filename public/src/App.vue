<script>
import { RouterLink, RouterView } from 'vue-router'

export default{
  data(){
    return{
      basket:[],
      showBasket:false,
    }
  },
  methods:{
    addToBasket(item){
      console.log(item)
      this.basket.push(item)
    }
  }
}


</script>

<template>
  <div class="container">
    <RouterView :basket="basket" :showBasket="showBasket" :addToBasket="addToBasket"/>
  </div>
</template>

<style>

</style>
