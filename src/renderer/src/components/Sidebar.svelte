<script lang="ts">
  import Sidebar from 'svelte_sidebar'

  const sidebar_props = {
    routes: [
      { name: 'Home', route: '/' },
      {
        name: 'Location',
        route: '/section1',
        disabled: true
      },
      {
        name: 'History',
        route: '/section2',
        disabled: true
      }
    ],
    activeUrl: '/',

    theme: {
      backgroundColor_nav: '#0E0E0E',
      maxWidth_nav: '14vw',
      minWidth_nav: '14vw'
    }
  }
</script>

<div>
  <Sidebar {...sidebar_props} />
  <!-- <h1>Rocket UI</h1>
  <h3>Documentation</h3> -->
</div>

<style>
  h1 {
    font-family: 'New Amsterdam', sans-serif;
    letter-spacing: 1.2px;
    /* default spacing is too small, smaller thann on google fonts */
  }
</style>
