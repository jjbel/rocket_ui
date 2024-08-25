<script lang="ts">
  import { onMount } from 'svelte'
  import Plotly from 'plotly.js-dist'

  onMount(() => {
    const TESTER = document.getElementById('tester')

    Plotly.newPlot(
      TESTER,
      [
        {
          x: [1, 2, 3, 4, 5],
          y: [1, 2, 4, 8, 16]
        }
      ],
      {
        margin: { t: 0 }
      }
    )
  })
</script>

<div>Caption</div>
