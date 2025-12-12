# Visual Design: Hashing and Sets/Maps

## Environment Overview

The Hashing world is set in a futuristic data center with a honeycomb-structured storage system. The environment emphasizes the mathematical transformation of hash functions and the spatial organization of buckets.

### Background and Atmosphere

The scene is a sleek, high-tech facility with dark metallic walls and ambient blue lighting. The central feature is a large honeycomb grid of hexagonal buckets that floats in the center of the space. A crystalline prism (the hash function) hovers above the grid, refracting incoming data into specific bucket locations.

### Lighting

Primary lighting comes from the glowing buckets themselves, creating a dynamic light map that shows table occupancy. The hash function prism emits rainbow refractions when processing keys. Collision events trigger warning amber glows.

### Camera Behavior

The camera can orbit 360 degrees around the honeycomb structure, zoom into individual buckets to see their contents, and follow the path of hash computations from key to bucket. A top-down view shows the overall distribution of elements across buckets.

### Interaction Ideas

Clicking on a bucket reveals its contents (key-value pairs or chain). Hovering over a key shows its hash value and bucket index. A "Hash Calculator" panel lets users input keys and see their hash values in real-time. Speed controls adjust animation pace for insertions and lookups.

---

## Sub-Concept 1: Hash Function and Bucket Mapping

### 3D Metaphor

The hash function is visualized as a floating crystalline prism. When a key is inserted, it enters the prism as a beam of light. Inside the prism, the key undergoes transformation (visible as swirling patterns), and exits as a focused beam that lands on a specific bucket.

**Hash Computation Animation**:
1. Key appears as a glowing text label
2. Key enters the prism from above
3. Inside the prism, mathematical operations are visualized as light patterns
4. A number (the hash value) emerges and is modulo-reduced to bucket index
5. A beam shoots down to illuminate the target bucket

**Good vs Bad Hash Functions**:
- Good hash: Beams spread evenly across all buckets
- Bad hash: Beams cluster in certain areas, leaving others empty

### Visual Elements

- Crystalline prism with internal light effects
- Beam paths from keys to buckets
- Hash value display during computation
- Bucket index calculation (hash % size)
- Distribution heat map overlay

---

## Sub-Concept 2: Separate Chaining

### 3D Metaphor

Each bucket is a hexagonal container that can hold a chain of elements. When multiple keys hash to the same bucket, they form a chain of glowing orbs extending outward from the bucket, like a string of pearls.

**Insertion with Collision**:
1. New key hashes to an occupied bucket
2. Collision alert: bucket flashes amber
3. New element becomes an orb that attaches to the existing chain
4. Chain extends outward from the bucket

**Lookup in Chain**:
1. Hash to bucket
2. Traverse chain: each orb lights up sequentially
3. Matching key found: orb glows green
4. Key not found: reach end of chain, red indicator

**Deletion from Chain**:
1. Find element in chain
2. Element orb detaches and dissolves
3. Chain reconnects (if middle element removed)

### Visual Elements

- Hexagonal bucket containers
- Chain of orbs extending from buckets
- Collision flash effect
- Chain traversal animation
- Chain length indicators

---

## Sub-Concept 3: Open Addressing (Linear Probing)

### 3D Metaphor

With open addressing, each bucket holds at most one element. When a collision occurs, the insertion beam bounces to the next bucket, leaving a visible trail. Linear probing creates straight trails as the beam moves sequentially through buckets.

**Linear Probing Insertion**:
1. Key hashes to bucket i
2. If occupied, beam bounces to bucket i+1
3. Continue bouncing until empty bucket found
4. Trail shows the probing sequence
5. Element settles into the empty bucket

**Lookup with Probing**:
1. Hash to initial bucket
2. If key doesn't match, follow probe sequence
3. Each checked bucket lights up
4. Stop when key found or empty bucket reached

**Clustering Visualization**:
- Clusters of consecutive occupied buckets glow as connected regions
- Shows how linear probing creates primary clustering
- Performance degrades as clusters grow

### Visual Elements

- Single-element buckets
- Bouncing beam animation
- Probe trail visualization
- Cluster highlighting
- Probe count display

---

## Sub-Concept 4: Open Addressing (Quadratic Probing)

### 3D Metaphor

Quadratic probing uses a curved, expanding probe sequence. The beam bounces in increasing jumps (1, 4, 9, 16...), creating an arc pattern that spreads elements more evenly than linear probing.

**Quadratic Probing Pattern**:
1. Initial hash to bucket i
2. First probe: i + 1
3. Second probe: i + 4
4. Third probe: i + 9
5. Curved trail shows the expanding pattern

**Comparison with Linear**:
- Side-by-side view of both probing methods
- Same insertions, different probe patterns
- Quadratic shows less clustering

### Visual Elements

- Curved probe trails
- Jump distance indicators (1, 4, 9, 16...)
- Comparison split-screen
- Reduced clustering visualization

---

## Sub-Concept 5: Load Factor and Resizing

### 3D Metaphor

The load factor is shown as a meter on the side of the honeycomb. As more elements are inserted, the meter fills up. When it crosses a threshold (typically 0.7), a resize operation triggers.

**Resize Animation**:
1. Load factor meter hits threshold
2. Warning: "Resize Required"
3. New, larger honeycomb materializes nearby
4. All elements rehash: beams shoot from old to new positions
5. Old honeycomb fades away
6. New honeycomb becomes primary

**Load Factor Effects**:
- Low load factor: Fast operations, sparse buckets
- High load factor: Slower operations, longer chains/probes
- Performance graph shows degradation curve

### Visual Elements

- Load factor meter (0.0 to 1.0)
- Threshold indicator line
- Resize animation with rehashing beams
- Performance impact visualization
- Before/after comparison

---

## Sub-Concept 6: Sets vs Maps

### 3D Metaphor

Sets and maps are shown as two variations of the honeycomb structure. Sets store only keys (single orbs), while maps store key-value pairs (orbs with attached data tags).

**Set Operations**:
- Add: Single orb inserted
- Contains: Search for orb
- Remove: Orb dissolves

**Map Operations**:
- Put: Orb with attached value tag inserted
- Get: Find orb, return value tag
- Update: Replace value tag on existing orb

**Set Operations (Union, Intersection, Difference)**:
- Two honeycombs side by side
- Union: Elements from both merge into new honeycomb
- Intersection: Only shared elements transfer
- Difference: Elements in first but not second transfer

### Visual Elements

- Single orbs for sets
- Orbs with value tags for maps
- Set operation animations
- Venn diagram overlay for set operations

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Blue-Gray | #1a1a2e |
| Empty bucket | Dim Gray | #2d2d44 |
| Occupied bucket | Soft Blue | #4a90d9 |
| Hash prism | Crystal White | #e8e8f0 |
| Hash beam | Rainbow gradient | varies |
| Collision warning | Amber | #f0a500 |
| Chain orbs | Cyan | #4ecdc4 |
| Found element | Success Green | #2ecc71 |
| Not found | Alert Red | #e74c3c |
| Probe trail | Purple | #9b59b6 |
| Load factor meter | Orange gradient | #f39c12 to #e74c3c |
| Set orbs | Teal | #1abc9c |
| Map value tags | Gold | #f1c40f |

---

## Animation Timing

- Hash computation in prism: 600ms
- Beam travel to bucket: 400ms
- Collision flash: 200ms
- Chain attachment: 300ms
- Chain traversal per node: 200ms
- Probe bounce: 250ms per hop
- Resize rehash per element: 150ms
- Load factor meter update: 300ms
- Set operation transfer: 200ms per element
- Camera transitions: 500ms ease-in-out
