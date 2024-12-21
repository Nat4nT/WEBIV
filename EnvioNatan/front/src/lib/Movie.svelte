<script>
    import { onMount } from "svelte";
    let results = $state(null);
    let debug = $state(false);
    //let debug = $state(true);
    async function getMovies() {
            
            let endpoint = `http://localhost:8000/top/movies`;
            
            let res = await fetch(endpoint);
            let data = await res.json();
            if (res.ok) {
                return data;
            } else {throw new Error(data); }
    }
    onMount(() => {
        getMovies().then((data)=>{
            results = data["results"]; 
        });
    });
</script>
    
<main>
    <h1>top 20 popular movies</h1>
    
    {#if results}
    <input style="display: none;" type="checkbox" bind:checked={debug}>
    {#if debug}
    <pre>{JSON.stringify(results[0], null, 2)}</pre>
    {/if}
    <div class="results">
        {#each results as movie }
        <p><img src="https://image.tmdb.org/t/p/w185/{movie.poster_path}" alt="{movie.title}"></p>
        <div>
            <h2>{ movie.title }</h2>
            <p>{ movie.release_date}</p>
        </div>
        {/each}
    </div>
    {/if}
</main>
        
<style>
    main{
        padding: 10px;
    }
    pre{
        white-space: pre-wrap;
    }
    .results{
        display:grid;
        gap: 10px;
        grid-template-columns: max-content max-content;
    }
</style>