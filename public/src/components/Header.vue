

<script>
export default{
    props:
        ["basket"],

    data(){
        return{
            showBasket:false,
        }
    },
}



</script>

<template>
<header>
    <img src="/img/logo.svg" alt="ауе">
    <ul>
        <li><RouterLink to="/" active-class="active">Main</RouterLink></li>
        <li><RouterLink to="/items" active-class="active">Products</RouterLink></li>
        <li><RouterLink to="/delivery" active-class="active">Delivery</RouterLink></li>
        <li><RouterLink to="/about" active-class="active">About us</RouterLink></li>
        <li><img src="/img/purchase.svg" @click="showBasket = !showBasket"></li>
    </ul>
    <div class="basket" v-if="showBasket">
        <div class="box"></div>

        <h3 v-if="basket.length == 0">Товаров нет</h3>
        <div class="items" v-else>
        <div class="item" v-for="el in basket" :key="el.slug">
            <img :src="'/img/' + el.image" :alt="el.title">
            <h3>{{ el.title }}</h3>
            <span>{{ el.price }}$</span>
        </div>
        <button>Перейти к оплате</button>
    </div>
    </div>
</header>
</template>

<style scoped>

.basket{
    position: absolute;
    top:50px;
    right: 0;
    padding: 20px;
    width: 250px;
    background-color: #B2BAC1;
    border-radius: 2px;
    z-index: 100;
}

.basket .box{
    position: absolute;
    background-color: #B2BAC1;
    top: -7px;
    right: 10px;
    width: 15px;
    height: 15px;
    transform: rotate(45deg);
}

header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;

}

header ul {
    list-style: none;
}

header ul li{
    display: inline;
    margin-left: 25px ;
    cursor: pointer;
}

header ul li .active{
    padding: 5px 15px;
    background-color: #B2BAC1;
    border-radius: 20px;
}

header ul li .active:hover{
    color:#fff;
    background-color: #616569;
}

header ul a{
    position: relative;
    bottom: 10px;
}
</style>

