<template>
  <div>
    <section>
      <base-card>
        <div>
          <base-button mode="outline" @click="cargaBuses"
            >Refrescar</base-button
          >
          <base-button v-if="!isLoading" link to="/busRegistro">
            Registrar Bus
          </base-button>
        </div>
        <div v-if="isLoading">
          <base-spinner></base-spinner>
        </div>
        <ul v-else>
          <bus-item
            v-for="bus in buses"
            :key="bus.id"
            :id="bus.id"
            :marca="bus.marca"
            :modelo="bus.modelo"
            :vigencia="bus.vigencia"
            :lugar="bus.lugar"
            @recargar-buses="cargaBuses"
          ></bus-item>
        </ul>
      </base-card>
    </section>
  </div>
</template>

<script>
import BusItem from "../../components/bus/BusItem.vue";
export default {
  components: {
    BusItem
  },
  data() {
    return {
      isLoading: false,
      error: null
    };
  },
  computed: {
    buses() {
      return this.$store.getters["buses/buses"];
    }
  },
  created() {
    this.cargaBuses();
  },
  methods: {
    async cargaBuses() {
      this.isLoading = true;
      try {
        await this.$store.dispatch("buses/cargaBuses");
      } catch (error) {
        console.log(error);
      }
      this.isLoading = false;
    }
  }
};
</script>

<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
</style>
