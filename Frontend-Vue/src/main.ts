import { createApp } from 'vue'
import App from './App.vue'
import libregl from 'libregl'
import 'maplibre-gl/dist/maplibre-gl.css'

const app = createApp(App)

app.use(libregl, {
  //
})
app.mount('#app')
