<script>
import Header from '../components/Header.vue'
export default{
    props:
    ["basket","showBasket"],
    components:{
        Header,
    }
}
</script>

<template>
<div>
    <Header :basket="basket" :showBasket="showBasket"></Header>
    <div>
        <h1>About delivery</h1>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim voluptatum illo libero maxime ducimus quisquam dolor officiis ea, aspernatur repellat reprehenderit, obcaecati error assumenda, deserunt eos similique voluptates natus earum.</p>
        <br>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim voluptatum illo libero maxime ducimus quisquam dolor officiis ea, aspernatur repellat reprehenderit, obcaecati error assumenda, deserunt eos similique voluptates natus earum.</p>
        <br>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim voluptatum illo libero maxime ducimus quisquam dolor officiis ea, aspernatur repellat reprehenderit, obcaecati error assumenda, deserunt eos similique voluptates natus earum.</p>
        
    </div>
</div>

</template>

<style scoped>
h1{
    margin-top: 150px ;
    font-weight: 400;
    font-size: 90px;
}

p{
    font-size: 18px;
    margin: 20px 0;
}

</style>