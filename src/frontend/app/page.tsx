'use client';

import React, { useEffect, useState, useCallback } from 'react';
import ReactFlow, { Controls, Background, useNodesState, useEdgesState, addEdge, Connection, Edge, Node } from 'reactflow';
import 'reactflow/dist/style.css';
import BlockNode from '@/components/BlockNode';
import { fetchBlocks, createPlaylistsFromComponents } from '@/lib/api';
import { Block } from '@/types';

const nodeTypes = { blockNode: BlockNode };

export default function Home() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [isCreating, setIsCreating] = useState(false);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  useEffect(() => {
    fetchBlocks().then(blocks => {
      const flowNodes = blocks.map((block, i) => ({
        id: block.name,
        position: { x: i * 250, y: 100 },
        data: block,
        type: 'blockNode',
      }));
      setNodes(flowNodes);
    });
  }, []);

  // Find all connected components in the graph
  const findConnectedComponents = useCallback(() => {
    if (edges.length === 0) {
      return [];
    }

    const adjacencyList = new Map<string, Set<string>>();
    
    // Build adjacency list (undirected graph)
    edges.forEach(edge => {
      if (!adjacencyList.has(edge.source)) {
        adjacencyList.set(edge.source, new Set());
      }
      if (!adjacencyList.has(edge.target)) {
        adjacencyList.set(edge.target, new Set());
      }
      adjacencyList.get(edge.source)!.add(edge.target);
      adjacencyList.get(edge.target)!.add(edge.source);
    });

    const visited = new Set<string>();
    const components: string[][] = [];

    // DFS to find connected components
    const dfs = (nodeId: string, component: string[]) => {
      visited.add(nodeId);
      component.push(nodeId);
      
      const neighbors = adjacencyList.get(nodeId);
      if (neighbors) {
        neighbors.forEach(neighbor => {
          if (!visited.has(neighbor)) {
            dfs(neighbor, component);
          }
        });
      }
    };

    // Find all components
    adjacencyList.forEach((_, nodeId) => {
      if (!visited.has(nodeId)) {
        const component: string[] = [];
        dfs(nodeId, component);
        components.push(component);
      }
    });

    return components;
  }, [edges]);

  // Create playlists for all connected components
  const createPlaylistsFromConnections = async () => {
    console.log('Button clicked!');
    console.log('Current nodes:', nodes);
    console.log('Current edges:', edges);
    
    setIsCreating(true);
    try {
      const components = findConnectedComponents();
      console.log('Found components:', components);
      
      if (components.length === 0) {
        alert('No connections found! Connect blocks first by dragging from one handle to another.');
        setIsCreating(false);
        return;
      }

      // Filter out single-node components
      const validComponents = components.filter(c => c.length > 1);
      console.log('Valid components (2+ blocks):', validComponents);
      
      if (validComponents.length === 0) {
        alert('No connected components found! You need at least 2 blocks connected.');
        setIsCreating(false);
        return;
      }

      // Create a payload with all connected components
      const payload = validComponents.map((component, index) => ({
        blockNames: component,
        playlistName: `Connected Playlist ${index + 1}`
      }));

      console.log('Sending payload:', payload);
      console.log('Making request to backend...');

      const result = await createPlaylistsFromComponents(payload);
      console.log('Result:', result);
      alert(`Successfully created ${validComponents.length} playlist(s)!`);
      
    } catch (error) {
      console.error('Error creating playlists:', error);
      alert(`Failed to create playlists. Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
    } finally {
      setIsCreating(false);
    }
  };

  return (
    <div className="w-screen h-screen bg-gray-50 relative">
    {/*  create playlist*/}
      <button
        onClick={createPlaylistsFromConnections}
        disabled={isCreating}
        className="absolute top-4 right-4 z-10 bg-green-600 hover:bg-green-700 disabled:bg-gray-400 text-white font-semibold py-2 px-6 rounded-lg shadow-lg transition-colors"
      >
        {isCreating ? 'Creating...' : 'Create Playlists from Connections'}
      </button>

      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
        nodesDraggable
        nodesConnectable
        edgesUpdatable
        proOptions={{ hideAttribution: true }}
      >
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}