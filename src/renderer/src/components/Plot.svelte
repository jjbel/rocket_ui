<script lang="ts">
  import { onMount } from 'svelte'
  import Plotly from 'plotly.js-dist'

  export let index
//   export let data
  export let caption = 'Caption'
  export let line_color = '#ffffff'

  onMount(() => {
    const plot_element = document.getElementById(index)

    console.log(line_color)

    Plotly.newPlot(
      plot_element,
      [
        {
          x: [],
          y: [],
          mode: 'lines', // lines+markers
          marker: {
            color: line_color,
            size: 8
          },
          line: {
            width: 5
          }
        }
      ],
      {
        // TODO need bottom and left to have margin for axes
        margin: { t: 0, b: 20, l: 20, r: 0 },
        plot_bgcolor: '#00000000',
        paper_bgcolor: '#000000',
        xaxis: {
          color: '#ffffff'
        },
        yaxis: {
          color: '#ffffff'
        },
        height: 300
      }
    )
  })

</script>

<div class="plot-parent">
  <div class="plot" id={index}></div>
  <div class="plot-caption">{caption}</div>
</div>

<style>
  .plot-parent {
    background-color: rgb(29, 29, 29);
    padding: 0.6rem;
    border-radius: 0.6rem;

    display: flex;
    flex-direction: column;
  }

  .plot-caption {
    text-align: center;
    margin: 0.6rem;
    font-size: 1.6rem;

    font-family: 'Source Code Pro', monospace;
    font-weight: 600;
  }
</style>
