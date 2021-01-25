<template>
    <tr>
        <td>{{nombre}}</td>
        <td>{{apellido}}</td>
        <td>{{rut}}</td>
        <td>{{ubicacion}}</td>
        <td>{{ choferVigente }}</td>
        <td>
          <button class="btn" v-if="deshabilitarBotton" @click="deshabilitarChofer" ><i class="fa fa-trash"></i></button>
          <button class="btn" @click="editarChofer"><i class="fa fa-list-ul"></i></button>
        </td>
    </tr>
</template>

<script>
export default {
  emits: ['recargar-choferes'],
  props: ['id', 'nombre', 'apellido', 'rut', 'ubicacion', 'vigencia'],
  computed: {
    urlEditar() {
      return `/choferEditar/${this.id}`;
    },
    choferVigente(){
      if(this.vigencia == 1){
        return 'Si'
      }
      return 'No'
    },
    deshabilitarBotton(){
      if(this.vigencia == 1){
        return true
      }
      return false
    }
  },
  methods: {
    editarChofer(){
      this.$router.push(this.urlEditar);
    },
    async deshabilitarChofer() {
      try {
        await this.$store.dispatch("choferes/deshabilitarChofer", this.id);
      } catch (error) {
        console.log(error);
      }
      this.$emit("recargar-choferes");
    }
  }
}
</script>

<style scoped>
td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 16px;
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  background-color: RoyalBlue;
}
</style>