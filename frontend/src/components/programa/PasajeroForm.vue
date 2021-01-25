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
      <p v-if="!nombre.isValid">Nombre no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !apellido.isValid }">
      <label for="apellido">Apellido </label>
      <input
        type="text"
        id="apellido"
        v-model.trim="apellido.val"
        @blur="limpiarValidacion('apellido')"
      />
      <p v-if="!apellido.isValid">Apellido no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !rut.isValid }">
      <label for="rut">Rut </label>
      <input
        type="text"
        id="rut"
        v-model.trim="rut.val"
        @blur="limpiarValidacion('rut')"
      />
      <p v-if="!rut.isValid">Rut no debe ir vacío.</p>
    </div>

    <div class="form-control" :class="{ invalid: !nReserva.isValid }">
      <label for="nReserva">Número de reserva</label>
      <select
        class="form-select"
        id="nReserva"
        v-model="nReserva.val"
        @blur="limpiarValidacion('nReserva')"
      >
        <option value="-1" selected disabled> Seleccionar </option>
        <option
          v-for="numero in numerosDisponibles"
          :key="numero"
          :value="numero"
        >
          {{ numero }}
        </option>
      </select>
      <p v-if="!nReserva.isValid">El número de reserva es obligatorio.</p>
    </div>

    <p v-if="!formValido">Favor completar el formulario y subir nuevamente.</p>
    <base-button>Registrar</base-button>
    <base-button @click.prevent="volver">Cancelar</base-button>
  </form>
</template>

<script>
export default {
  emits: ["guardar"],
  data() {
    return {
      idPrograma: "",
      idPasajero: "",
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
      nReserva: {
        val: "-1",
        isValid: true
      },
      numeros: [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20
      ],
      formValido: true
    };
  },
  computed: {
    numerosDisponibles() {
      var numerosDisponibles = this.numeros;
      this.$store.getters["programas/pasajeros"].forEach(element => {
        if (element.id != this.idPasajero) {
          const index = numerosDisponibles.indexOf(element.nReserva);
          numerosDisponibles.splice(index, 1);
        }
      });
      return numerosDisponibles;
    }
  },
  created() {
    if (this.$route.params.id) {
      this.idPrograma = this.$route.params.id;
    }

    if (this.$route.params.idPasajero) {
      this.idPasajero = this.$route.params.idPasajero;
    }
  },
  methods: {
    validoForm() {
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
      if (this.nReserva.val === "-1") {
        this.nReserva.isValid = false;
        this.formValido = false;
      }
    },
    limpiarValidacion(input) {
      this[input].isValid = true;
    },
    submitForm() {
      this.validoForm();
      if (!this.formValido) {
        return;
      }
      var formData = {};
      formData = {
        nombre: this.nombre.val,
        apellido: this.apellido.val,
        rut: this.rut.val,
        nReserva: this.nReserva.val,
        reservaId: this.idPrograma
      };

      this.$emit("guardar", formData);
    },
    volver() {
      this.$router.replace("/programas");
    }
  }
};
</script>

<style scoped>
.form-control {
  margin: 0.5rem 0;
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
