<script>
import Header from '../components/Header.vue'
import MainSection from '../components/MainSection.vue'

export default {
  props: ['basket','showBasket'],
  components: { Header, MainSection }
}
</script>

<template>
  <div>
    <Header :basket="basket" :showBasket="showBasket" />
    <MainSection />
  </div>
</template>
