import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default defineConfig({
   plugins: [react()],
  base:"/Build_DRF_PDF/"
  // build: {
  //   outDir: 'dist', // Output directory for production build
  // },
  
 

});

