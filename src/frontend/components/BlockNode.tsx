'use client';

import { Handle, Position } from 'reactflow';
import { Song } from '@/types';

export default function BlockNode({ data }: { data: any }) {
  return (
    <div className="bg-white border-2 border-black-300 rounded-lg shadow-md p-4 w-64 max-h-80 overflow-hidden">
      <Handle type="target" position={Position.Top} className="w-3 h-3 bg-blue-500" />
      
      <h3 className="font-bold text-lg mb-2 truncate text-black">{data.name.replace('blocks_', '')}</h3>
      <p className="text-sm text-gray-600 mb-2">Songs: {data.songCount}</p>
      
      <div className="space-y-1 max-h-40 overflow-y-auto">
        {Array.isArray(data.songs) && data.songs.length > 0 ? (
        data.songs.map((song: Song) => (
          <a
            key={song.id}
            href={song.link}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 hover:underline text-sm block truncate"
          >
            {song.name}
          </a>
        ))) : (
          <p className="text-gray-400 italic text-sm"> No songs available</p>
        )
      }
      </div>

      <Handle type="source" position={Position.Bottom} className="w-3 h-3 bg-green-500" />
    </div>
  );
}