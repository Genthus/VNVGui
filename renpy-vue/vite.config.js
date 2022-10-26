import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-electron-plugin'

// https://vitejs.dev/config/
export default defineConfig(({command, mode, ssrBuild }) => {
  if (command === 'serve') {
    return {
      server: {
        hmr: true,
        watch: {
          usePolling:true
        }
      },
      plugins: [
        vue()
      ]
    }
  } else {
    return {
      server: {
        hmr: true,
        watch: {
          usePolling:true
        }
      },
      plugins: [
        vue(),
        electron({
          include: ['electron'],
          transformOptions: {
            sourcemap: !!process.env.VSCODE_DEBUG,
          }
        }),
      ]
    }
  }
})