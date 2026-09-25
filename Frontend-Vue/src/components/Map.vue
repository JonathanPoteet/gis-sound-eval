<script setup lang="ts">
import { Map } from 'libregl'
import type { LngLatLike } from 'maplibre-gl'

interface Props {
  center?: LngLatLike
  zoom?: number
  bearing?: number
  style?: string
  height?: string
}

withDefaults(defineProps<Props>(), {
  center: () => [18, 48],
  zoom: 4,
    style: 'https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json',
  height: '100vh',
})

const emit = defineEmits(['load'])
</script>

<template>
  <Map
    :height
    width="100%"
    :center="center"
    :zoom="zoom"
    :style="style"
    @load="emit('load', $event)"
  >
    <slot></slot>
  </Map>
</template>