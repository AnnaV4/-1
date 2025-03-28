import { defineConfig } from 'vite'
import reactRefresh from '@vitejs/plugin-react-refresh'

export default defineConfig({
  plugins: [reactRefresh()],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @import '~bootstrap/scss/bootstrap';
        `
      }
    }
  }
})