# 3D Generator Prompts: Hashing and Sets/Maps

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Hash Table as Honeycomb Grid

Generate a 360-degree, interactive 3D scene showing a hash table as a honeycomb grid of hexagonal buckets. The environment is a futuristic data center with dark metallic walls (#1a1a2e) and ambient blue lighting.

Create a floating honeycomb structure with 16 hexagonal cells (4x4 arrangement). Each cell is a bucket that can hold elements. Empty buckets glow dimly (#2d2d44), while occupied buckets glow with soft blue (#4a90d9). Above the honeycomb, position a crystalline prism that represents the hash function.

**Hash Function Visualization**:
When a key is inserted:
1. The key appears as glowing text above the prism
2. The key enters the prism and undergoes transformation (swirling light patterns inside)
3. A hash value number emerges below the prism
4. The hash value is reduced modulo 16 to get the bucket index
5. A beam of light shoots down to illuminate the target bucket
6. The element settles into the bucket as a glowing orb

Include a control panel with:
- Input field for entering keys
- "Insert" button that triggers the hash animation
- "Lookup" button that searches for a key
- Hash value display showing the computation

The camera can orbit 360 degrees around the honeycomb, zoom into individual buckets, and follow hash beam paths. Add a distribution heat map overlay option showing bucket occupancy levels.

---

## Prompt 2: Separate Chaining Collision Resolution

Generate a 360-degree, interactive 3D scene demonstrating separate chaining for hash table collision resolution. The honeycomb grid has 8 buckets, and we will show multiple elements hashing to the same bucket.

Start with an empty hash table. Insert the following keys in sequence: "apple", "banana", "cherry", "apricot" (where "apple" and "apricot" hash to the same bucket).

**Collision Animation**:
1. "apple" hashes to bucket 3, settles as a cyan orb (#4ecdc4)
2. "banana" hashes to bucket 7, settles normally
3. "cherry" hashes to bucket 1, settles normally
4. "apricot" hashes to bucket 3 - COLLISION!
   - Bucket 3 flashes amber (#f0a500)
   - "Collision Detected" message appears
   - New orb attaches to existing orb, forming a chain
   - Chain extends outward from the bucket

**Chain Visualization**:
- Each element in a chain is a glowing orb with its key displayed
- Orbs are connected by thin glowing lines
- Chain length is shown as a number badge on the bucket

**Lookup Animation**:
When searching for "apricot":
1. Hash to bucket 3
2. First orb ("apple") lights up - not a match
3. Second orb ("apricot") lights up - MATCH FOUND (green glow)

Include a "worst case" demonstration showing all elements hashing to the same bucket, creating a long chain (O(n) lookup).

---

## Prompt 3: Linear Probing Collision Resolution

Generate a 360-degree, interactive 3D scene demonstrating linear probing for open addressing collision resolution. The hash table has 11 buckets arranged in a circular pattern.

Each bucket can hold exactly one element. When a collision occurs, the insertion beam bounces to the next bucket, leaving a visible purple trail (#9b59b6).

**Linear Probing Sequence**:
Insert keys that cause collisions:
1. Key A hashes to bucket 5, settles normally
2. Key B hashes to bucket 5 - collision!
   - Beam bounces to bucket 6 (empty), settles there
   - Trail shows: 5 -> 6
3. Key C hashes to bucket 5 - collision!
   - Beam bounces: 5 (occupied) -> 6 (occupied) -> 7 (empty)
   - Trail shows: 5 -> 6 -> 7
4. Key D hashes to bucket 6 - collision!
   - Beam bounces: 6 -> 7 -> 8 (empty)
   - Trail shows: 6 -> 7 -> 8

**Clustering Visualization**:
- Consecutive occupied buckets glow as a connected cluster
- Cluster regions are highlighted with a subtle outline
- "Primary Clustering" label appears when clusters form
- Performance meter shows degradation as clusters grow

**Lookup with Probing**:
When searching for Key C:
1. Hash to bucket 5
2. Check bucket 5 - not Key C, continue probing
3. Check bucket 6 - not Key C, continue probing
4. Check bucket 7 - FOUND! Green highlight

Include probe count display showing how many buckets were checked.

---

## Prompt 4: Quadratic Probing Comparison

Generate a 360-degree, interactive 3D scene with a split view comparing linear probing (left) and quadratic probing (right). Both hash tables have 16 buckets.

Insert the same sequence of keys into both tables simultaneously to show how probe patterns differ.

**Linear Probing (Left)**:
- Probe sequence: i, i+1, i+2, i+3, ...
- Straight probe trails
- Shows primary clustering

**Quadratic Probing (Right)**:
- Probe sequence: i, i+1, i+4, i+9, i+16, ...
- Curved, expanding probe trails
- Shows reduced clustering

**Visual Comparison**:
- Same keys inserted in same order
- Different final positions due to different probing
- Cluster size comparison display
- Average probe length comparison

**Probe Trail Visualization**:
- Linear: Straight purple lines
- Quadratic: Curved arcs with increasing jump distances
- Jump distance labels (1, 4, 9, 16) on quadratic trails

Include a "Probe Efficiency" meter for each table showing average probes per operation.

---

## Prompt 5: Load Factor and Dynamic Resizing

Generate a 360-degree, interactive 3D scene showing how load factor affects hash table performance and triggers resizing. Start with a hash table of 8 buckets.

**Load Factor Meter**:
- Vertical meter on the side showing load factor (0.0 to 1.0)
- Green zone: 0.0 - 0.5 (good performance)
- Yellow zone: 0.5 - 0.7 (acceptable)
- Red zone: 0.7 - 1.0 (poor performance, resize needed)
- Threshold line at 0.75

**Progressive Insertion**:
Insert elements one by one, showing:
1. Load factor meter rising with each insertion
2. Performance indicator showing average lookup time
3. Chain lengths or probe distances increasing

**Resize Animation** (when load factor exceeds 0.75):
1. "Resize Triggered" alert appears
2. New honeycomb (16 buckets) materializes to the right
3. Each element in old table rehashes:
   - Beam shoots from old position through prism
   - New hash computed for larger table
   - Beam lands on new bucket position
4. Old honeycomb fades away
5. New honeycomb moves to center
6. Load factor meter resets to ~0.375

**Before/After Comparison**:
- Show element distribution before resize (clustered)
- Show element distribution after resize (spread out)
- Performance improvement visualization

---

## Prompt 6: Sets and Maps Comparison

Generate a 360-degree, interactive 3D scene with two honeycomb structures side by side: a Set (left) and a Map (right).

**Set Visualization (Left)**:
- Each element is a single glowing teal orb (#1abc9c)
- Orbs contain only the key value
- Operations: add, contains, remove

**Map Visualization (Right)**:
- Each element is an orb with an attached golden tag (#f1c40f)
- Orb shows the key, tag shows the value
- Operations: put, get, update, remove

**Demonstration Sequence**:
1. Set.add("apple") - teal orb appears
2. Map.put("apple", 5) - orb with "5" tag appears
3. Set.add("banana") - another teal orb
4. Map.put("banana", 3) - orb with "3" tag
5. Map.update("apple", 10) - tag changes from "5" to "10"
6. Set.contains("apple") - orb highlights green
7. Map.get("banana") - orb highlights, tag value "3" displayed prominently

**Set Operations Panel**:
Show union, intersection, and difference with two sets:
- Set A: {1, 2, 3, 4}
- Set B: {3, 4, 5, 6}
- Union: {1, 2, 3, 4, 5, 6} - all orbs merge
- Intersection: {3, 4} - only shared orbs remain
- Difference (A-B): {1, 2} - orbs in A but not B

Include Venn diagram overlay showing set relationships.

---

## Prompt 7: Real-World Application - Two Sum Problem

Generate a 360-degree, interactive 3D scene showing how a hash map solves the Two Sum problem efficiently. The problem: find two numbers in an array that add up to a target sum.

**Setup**:
- Array displayed as a row of numbered blocks: [2, 7, 11, 15]
- Target sum: 9
- Empty hash map (honeycomb) below the array

**Naive Approach (O(n^2)) - Brief Comparison**:
- Show nested loops checking all pairs
- Many comparisons highlighted
- "Inefficient" label

**Hash Map Approach (O(n))**:
1. Process element 2:
   - Need 9-2=7 to complete sum
   - Check hash map for 7 - not found
   - Store {2: index 0} in hash map
   
2. Process element 7:
   - Need 9-7=2 to complete sum
   - Check hash map for 2 - FOUND at index 0!
   - Highlight: indices [0, 1] are the answer
   - "Solution Found!" celebration

**Visualization Elements**:
- Array with current element highlighted
- "Complement needed" calculation display
- Hash map showing stored values
- Lookup beam when checking for complement
- Success animation when pair found

Include complexity comparison: O(n^2) vs O(n) with visual representation.

---

## General Requirements for All Prompts

- All scenes must support 360-degree camera orbit and zoom in/out functionality
- Include educational labels with readable fonts (minimum 14pt equivalent in 3D space)
- Use color coding consistently across all scenes as defined in the color palette
- Ensure interactive elements have clear hover states and click feedback
- Animations should be smooth (60fps target) with adjustable speed controls
- Include accessibility considerations: high contrast mode option, colorblind-friendly palette alternative
- All text labels should remain readable from any camera angle (billboard text or smart orientation)
- Export scenes in formats compatible with web embedding (glTF, WebGL-ready)
- Include corresponding Python code snippets that highlight during relevant animation steps
- Add sound effects for hash computations and collisions (optional toggle)
