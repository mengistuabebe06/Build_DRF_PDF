import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base:"/Build_DRF_PDF/frontend/",
  plugins: [react()],

})
