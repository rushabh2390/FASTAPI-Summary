<template>
<div class="container" >
  {{ title }}
  <div class="card" style="width: 100%;">
  <div class="card-header">
    <form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <div class="row">
          <table class="table-primary">
            <tr>
              <td>
                <div class="col-md-8">
                  <label for="formFile" class="form-label">
                    Upload your file(docx, pdf, txt, utf only)
                  </label>
                  <input class="form-control-file" type="file" id="formFile" @change="onFileChange">
                </div>
              </td>
              <td>
                <div class="col-md-4">
                  <button  class="btn btn-primary mb-2" >Submit</button>
                </div>
              </td>
            </tr>
          </table>
        </div>
    </form>
  </div>
    <div class="card-body">
      <div class="row">
      <div class="col-md-12" v-if="message!=null">
        <h5> {{ message }} </h5>
      </div>
      </div>
      <div class="row"  v-if="metadata!=null">
        <h5 class="text-md-left">Probable Metadata</h5>
        <div class="col-md-12">
          <p class="text-md-left" >{{ metadata }}</p>
        </div>
      </div>
      <div class="row"  v-if="summary!=null">
        <h5 class="text-md-left">Probable Summary</h5>
        <div class="col-md-12" >
          <p class="text-md-left" >{{ summary }}</p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import Axios from 'axios'

export default {
  name: 'FileUpload',
  data () {
    return {
      file: null,
      message: null,
      response: null,
      metadata: null,
      summary: null,
      title: null,
    }
  },
  created() {
    this.title = config.VUE_APP_TITLE  || process.env.VUE_APP_TITLE || "MetaData & Summary Generator"
    Axios.defaults.baseURL = config.VUE_APP_API_BACKEND || process.env.VUE_APP_API_BACKEND || "http://localhost:8000"
  },
  methods: {
    async onSubmit () {
      const formData = new FormData()
      formData.append('file', this.file)
      try {
        const headers = { 'Content-Type': 'multipart/form-data', 'accept': 'application/json' }
        const response = await Axios.post('/uploadfile', formData, { headers })
        this.metadata = response.data['probable metadata']
        this.summary = response.data['probable summary']
        this.message = null
      } catch (err) {
        this.message = err
        this.metadata = null
        this.summary = null
      }
    },
    async onFileChange (e) {
      const selectedFile = e.target.files[0]
      this.file = selectedFile
    }
  }
}
</script>
