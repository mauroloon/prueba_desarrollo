<template>
  <form @submit.prevent="submitForm">
    <div class="form-control" :class="{ invalid: !nombre.isValid }">
      <label for="nombre">Nombre </label>
      <input
        type="text"
        id="nombre"
        v-model.trim="nombre.val"
        @blur="limpiarValidacion('nombre')"
      />
      <p v-if="!nombre.isValid">nombre no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !apellido.isValid }">
      <label for="apellido">Apellido </label>
      <input
        type="text"
        id="apellido"
        v-model.trim="apellido.val"
        @blur="limpiarValidacion('apellido')"
      />
      <p v-if="!apellido.isValid">apellido no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !rut.isValid }">
      <label for="rut">rut </label>
      <input
        type="text"
        id="rut"
        v-model.trim="rut.val"
        @blur="limpiarValidacion('rut')"
      />
      <p v-if="!rut.isValid">rut no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !ubicacion.isValid }">
      <label for="ubicacion">Ubicación </label>
      <select
        id="ubicacion"
        v-model="ubicacion.val"
        @blur="limpiarValidacion('ubicacion')"
        class="form-select"
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
      <select
        class="form-select"
        v-model="vigencia.val"
        @blur="limpiarValidacion('vigencia')"
      >
        <option value="1"> Si </option>
        <option value="0"> No </option>
      </select>
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
      idChofer: "",
      nombre: {
        val: "",
        isValid: true
      },
      apellido: {
        val: "",
        isValid: true
      },
      rut: {
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
      this.idChofer = this.$route.params.id;
      this.cargarChofer();
    }
  },
  methods: {
    validarForm() {
      this.formValido = true;
      if (this.nombre.val === "") {
        this.nombre.isValid = false;
        this.formValido = false;
      }
      if (this.apellido.val === "") {
        this.apellido.isValid = false;
        this.formValido = false;
      }
      if (this.rut.val === "") {
        this.rut.isValid = false;
        this.formValido = false;
      }
      if (this.ubicacion.val === "-1") {
        this.ubicacion.isValid = false;
        this.formIsValid = false;
      }
    },
    limpiarValidacion(input) {
      this[input].isValid = true;
    },
    async cargarLugares() {
      try {
        await this.$store.dispatch("buses/cargarLugares");
      } catch (error) {
        console.log(error);
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
          id: this.idChofer,
          nombre: this.nombre.val,
          apellido: this.apellido.val,
          rut: this.rut.val,
          lugar: this.ubicacion.val,
          vigencia: this.vigencia.val
        };
        this.$emit("editar", formData);
      } else {
        formData = {
          nombre: this.nombre.val,
          apellido: this.apellido.val,
          rut: this.rut.val,
          lugar: this.ubicacion.val
        };
        this.$emit("guardar", formData);
      }
    },
    async cargarChofer() {
      const response = await fetch(
        `http://localhost:8000/v1/bus/chofer/${this.idChofer}/`
      );
      const responseData = await response.json();

      if (responseData.code == 1) {
        this.nombre.val = responseData.data.CFR_NOMBRE;
        this.apellido.val = responseData.data.CFR_APELLIDO;
        this.rut.val = responseData.data.CFR_RUT;
        this.ubicacion.val = responseData.data.LGR_ID.LGR_ID;
        this.vigencia.val = responseData.data.CFR_VIGENCIA;
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
.form-select {
  display: block;
  height: 34px;
  padding: 6px 12px;
  font-size: 14px;
  color: #555;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
</style>
