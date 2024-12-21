<script>
    import { onMount } from "svelte";

    let results = $state(null);
    let debug = $state(false);
    let searchQuery = $state(); 
    let searchType = $state(); 

    async function getPersons(query, type) {
        let endpoint = type === "id"
            ? `http://localhost:8000/id_person/${encodeURIComponent(query)}`
            : `http://localhost:8000/person/${encodeURIComponent(query)}`;

        try {
            const res = await fetch(endpoint);
            const data = await res.json();
            if (res.ok) {
                results = type === "id" ? [data] : data["results"];
            } else {
                throw new Error(data);
            }
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
            results = null;
        }
    }

    onMount(() => {
        getPersons(searchQuery, searchType);
    });
</script>

<main>
    <h1>Lista de Artistas</h1>

    
    <input
        type="text"
        placeholder="Digite o nome ou ID"
        bind:value={searchQuery}
        oninput={() => getPersons(searchQuery, searchType)} />

    <input type="checkbox" bind:checked={debug}>
    
    <div>
        <label>
            <input type="radio" value="name" bind:group={searchType} onchange={() => getPersons(searchQuery, searchType)} />
            Buscar por Nome
        </label>
        <label>
            <input type="radio" value="id" bind:group={searchType} onchange={() => getPersons(searchQuery, searchType)} />
            Buscar por ID
        </label>
    </div>

    {#if debug && results}
        <pre>{JSON.stringify(results, null, 2)}</pre>
    {/if}

    {#if results}
        <div class="results">
            {#each results as person}
                <div>
                    <h2>{person.name}</h2>
                    <p>Id: {person.id}</p>
                </div>
            {/each}
        </div>
    {:else}
        <p>Nenhum resultado encontrado.</p>
    {/if}
</main>

<style>
    main {
        padding: 10px;
    }
    pre {
        white-space: pre-wrap;
        background: #f0f0f0;
        padding: 10px;
    }
    .results {
        display: grid;
        gap: 10px;
        grid-template-columns: max-content max-content;
    }
    input[type="text"] {
        margin-bottom: 10px;
        padding: 5px;
        width: 300px;
    }
    label {
        margin-right: 10px;
    }
</style>
