<script>
    import "./app.css"
    let { children } = $props();
</script>
    
<nav>
    <a href="/">home</a>
    <a href="/movies">filmes</a>
    <a href="/favoritos">favoritos</a>
    <a href="person">artistas</a>
</nav>
    
{@render children()}