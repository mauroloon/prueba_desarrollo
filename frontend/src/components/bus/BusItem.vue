<template>
  <li>
    <h3>Marca: {{ marca }}</h3>
    <h4>Modelo: {{ modelo }} | Vigente: {{ vigenciaRules }}</h4>
    <h5>
      Ubicación del bus: {{ lugar.LGR_NOMBRE }}, {{ lugar.LGR_DESCRIPCION }}
    </h5>
    <div class="actions">
      <base-button
        v-if="deshabilitarBoton"
        mode="danger"
        @click="deshabilitarBus"
        >Deshabilitar</base-button
      >
      <base-button link :to="editar">Editar</base-button>
    </div>
  </li>
</template>

<script>
export default {
  emits: ["recargar-buses"],
  props: ["id", "marca", "modelo", "vigencia", "lugar"],
  computed: {
    editar() {
      return `/busEditar/${this.id}`;
    },
    vigenciaRules() {
      if (this.vigencia == 1) {
        return "Si";
      } else {
        return "No";
      }
    },
    deshabilitarBoton() {
      if (this.vigencia == 1) {
        return true;
      }
      return false;
    }
  },
  methods: {
    async deshabilitarBus() {
      try {
        await this.$store.dispatch("buses/deshabilitarBus", this.id);
      } catch (error) {
        console.log(error);
      }
      this.$emit("recargar-buses");
    }
  }
};
</script>

<style scoped>
li {
  margin: 1rem 0;
  border: 1px solid #424242;
  border-radius: 12px;
  padding: 1rem;
}

h3 {
  font-size: 1.5rem;
}

h3,
h4 {
  margin: 0.5rem 0;
}

div {
  margin: 0.5rem 0;
}

.actions {
  display: flex;
  justify-content: flex-end;
}
</style>
