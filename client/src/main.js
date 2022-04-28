import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/display.css'
import ru from "element-plus/es/locale/lang/ru";
import App from './App.vue'

createApp(App).use(ElementPlus, {
    locale: ru,
}).mount('#app')
