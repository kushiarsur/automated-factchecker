import React from 'react'

function CommentSection({ comments }) {
  const formatTimeAgo = (dateString) => {
    const date = new Date(dateString)
    const seconds = Math.floor((new Date() - date) / 1000)
    if (seconds < 60) return 'just now'
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m`
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h`
    if (seconds < 604800) return `${Math.floor(seconds / 86400)}d`
    return date.toLocaleDateString()
  }

  if (comments.length === 0) {
    return <p className="text-sm text-gray-500 text-center py-4">No comments yet. Be the first to comment!</p>
  }

  return (
    <div className="mt-4 space-y-3 max-h-64 overflow-y-auto">
      {comments.map((comment) => (
        <div key={comment.id} className="flex items-start space-x-3 animate-fade-in">
          <img
            src={comment.avatar_url || `https://ui-avatars.com/api/?name=${comment.username}&background=9333ea&color=fff`}
            alt={comment.username}
            className="w-8 h-8 rounded-full flex-shrink-0"
          />
          <div className="flex-1 min-w-0">
            <div className="bg-gray-50 rounded-2xl px-4 py-2">
              <p className="font-semibold text-sm text-gray-900">{comment.username}</p>
              <p className="text-sm text-gray-800 mt-0.5 break-words">{comment.content}</p>
            </div>
            <div className="flex items-center space-x-4 mt-1 px-2">
              <span className="text-xs text-gray-500">{formatTimeAgo(comment.created_at)}</span>
              <button className="text-xs text-gray-600 hover:text-red-500 font-semibold">Like</button>
              {comment.likes > 0 && (
                <span className="text-xs text-gray-500">{comment.likes} {comment.likes === 1 ? 'like' : 'likes'}</span>
              )}
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

export default CommentSection
