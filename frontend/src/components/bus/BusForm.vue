<template>
  <form @submit.prevent="submitForm">
    <div class="form-control" :class="{ invalid: !marca.isValid }">
      <label for="marca">marca</label>
      <input
        type="text"
        id="marca"
        v-model.trim="marca.val"
        @blur="limpiarValidacion('marca')"
      />
      <p v-if="!marca.isValid">marca no debe ir vacía.</p>
    </div>
    <div class="form-control" :class="{ invalid: !modelo.isValid }">
      <label for="modelo">modelo</label>
      <input
        type="text"
        id="modelo"
        v-model.trim="modelo.val"
        @blur="limpiarValidacion('modelo')"
      />
      <p v-if="!modelo.isValid">modelo no debe ir vacío.</p>
    </div>
    <div class="form-control" :class="{ invalid: !ubicacion.isValid }">
      <label for="ubicacion">Ubicación</label>
      <select
        id="ubicacion"
        v-model="ubicacion.val"
        @blur="limpiarValidacion('ubicacion')"
      >
        <option value="-1" selected> Seleccionar </option>
        <option v-for="lugar in lugares" :key="lugar.id" :value="lugar.id">
          {{ lugar.nombre }}
        </option>
      </select>
      <p v-if="!ubicacion.isValid">La ubicación es obligatoria.</p>
    </div>

    <div class="form-control" v-if="modoEdit">
      <label for="modelo">Vigente</label>
      <select v-model="vigencia.val" @blur="limpiarValidacion('vigencia')">
        <option value="1"> Si </option>
        <option value="0"> No </option>
      </select>
      <p v-if="!ubicacion.isValid">La vigencia es obligatoria.</p>
    </div>

    <p v-if="!formValido">Favor completar el formulario y subir nuevamente.</p>
    <base-button v-if="!modoEdit">Registrar</base-button>
    <base-button v-else>Editar</base-button>
  </form>
</template>

<script>
export default {
  emits: ["guardar", "editar"],
  data() {
    return {
      idBus: "",
      marca: {
        val: "",
        isValid: true
      },
      modelo: {
        val: "",
        isValid: true
      },
      ubicacion: {
        val: "-1",
        isValid: true
      },
      vigencia: {
        val: "-1",
        isValid: true
      },
      formValido: true,
      modoEdit: false
    };
  },
  computed: {
    lugares() {
      const lugares = this.$store.getters["buses/lugares"];
      return lugares;
    }
  },
  created() {
    this.cargarLugares();
    if (this.$route.params.id) {
      this.modoEdit = true;
      this.idBus = this.$route.params.id
      this.cargarBus();
    }
  },
  methods: {
    limpiarValidacion(input) {
      this[input].isValid = true;
    },
    validarForm() {
      this.formValido = true;
      if (this.marca.val === "") {
        this.marca.isValid = false;
        this.formValido = false;
      }
      if (this.modelo.val === "") {
        this.modelo.isValid = false;
        this.formValido = false;
      }
      if (this.ubicacion.val === "-1") {
        this.ubicacion.isValid = false;
        this.formIsValid = false;
      }
    },
    submitForm() {
      this.validarForm();

      if (!this.formValido) {
        return;
      }
      var formData = {};
      if (this.modoEdit) {
        formData = {
          id: this.idBus,
          marca: this.marca.val,
          modelo: this.modelo.val,
          lugar: this.ubicacion.val,
          vigencia: this.vigencia.val
        };
        this.$emit("editar", formData);
      } else {
        formData = {
          marca: this.marca.val,
          modelo: this.modelo.val,
          lugar: this.ubicacion.val
        };

        this.$emit("guardar", formData);
      }
    },
    async cargarLugares() {
      try {
        await this.$store.dispatch("buses/cargarLugares");
      } catch (error) {
        console.log(error);
      }
    },
    async cargarBus() {
      const response = await fetch(`http://localhost:8000/v1/bus/bus/${this.idBus}/`);
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.marca.val = responseData.data.BUS_MARCA;
        this.modelo.val = responseData.data.BUS_MODELO;
        this.ubicacion.val = responseData.data.LGR_ID.LGR_ID;
        this.vigencia.val = responseData.data.BUS_VIGENCIA;
      }
    }
  }
};
</script>

<style scoped>
.form-control {
  margin: 0.5rem 0;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input[type="checkbox"] + label {
  font-weight: normal;
  display: inline;
  margin: 0 0 0 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  border: 1px solid #ccc;
  font: inherit;
}

input:focus,
textarea:focus {
  background-color: #f0e6fd;
  outline: none;
  border-color: #c1c0c4;
}

input[type="checkbox"] {
  display: inline;
  width: auto;
  border: none;
}

input[type="checkbox"]:focus {
  outline: #b8b6bb solid 1px;
}

h3 {
  margin: 0.5rem 0;
  font-size: 1rem;
}

.invalid label {
  color: red;
}

.invalid input,
.invalid textarea {
  border: 1px solid red;
}
</style>
