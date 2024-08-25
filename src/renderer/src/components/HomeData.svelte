<script lang="ts">
  import Plot from './Plot.svelte'
</script>

<div class="homedata">
  <Plot index="1" caption="Acceleration" line_color="#1d41fe" />
  <Plot index="2" caption="Temperature" line_color="#ff0808" />
  <Plot index="3" caption="Height" line_color="#00ff78" />
  <Plot index="4" caption="Throttle" line_color="#9319ff" />
</div>

<style>
  .homedata {
    /* see sidebar width! */
    width: 86vw;
    /* https://stackoverflow.com/questions/9811465/scrollable-div-inside-container */
    height: 100vh;
    padding: 0.6rem;
    overflow: scroll;

    display: grid;
    /* grid-template-rows: repeat(2, 1fr); */
    grid-template-columns: repeat(2, 1fr);
    grid-column-gap: 0.6rem;
    grid-row-gap: 0.6rem;
  }
</style>
