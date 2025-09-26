<script>
import { Link } from "@inertiajs/svelte";
</script>

<div>
    <nav class="flex items-start justify-center">
        <ul class="flex space-x-4">
            <li><Link href="/">Home</Link></li>
        </ul>
    </nav>
    <div class="flex items-center justify-center mt-32">
        <slot />
    </div>
</div>
