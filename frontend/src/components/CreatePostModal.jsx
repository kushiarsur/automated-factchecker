import React, { useState, useRef } from 'react'
import { X, Image as ImageIcon, Loader2, Upload, Trash2 } from 'lucide-react'
import { createPost } from '../services/api'
import { getUser } from '../utils/auth'

function CreatePostModal({ onClose, onPostCreated }) {
  const user = getUser()
  const [caption, setCaption] = useState('')
  const [imageFile, setImageFile] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [creating, setCreating] = useState(false)
  const [error, setError] = useState('')
  const [dragOver, setDragOver] = useState(false)
  const fileInputRef = useRef(null)

  const handleFileChange = (file) => {
    if (!file) return
    if (!file.type.startsWith('image/')) {
      setError('Please select an image file (JPG, PNG, GIF, WebP)')
      return
    }
    if (file.size > 10 * 1024 * 1024) {
      setError('Image must be smaller than 10MB')
      return
    }
    setError('')
    setImageFile(file)
    const previewUrl = URL.createObjectURL(file)
    setImagePreview(previewUrl)
  }

  const handleInputChange = (e) => {
    const file = e.target.files[0]
    if (file) handleFileChange(file)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setDragOver(false)
    const file = e.dataTransfer.files[0]
    if (file) handleFileChange(file)
  }

  const removeImage = () => {
    setImageFile(null)
    if (imagePreview) URL.revokeObjectURL(imagePreview)
    setImagePreview(null)
    if (fileInputRef.current) fileInputRef.current.value = ''
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    if (!caption.trim()) { setError('Please enter a caption'); return }
    setCreating(true)
    try {
      let imageDataUrl = null
      if (imageFile) {
        imageDataUrl = await new Promise((resolve) => {
          const reader = new FileReader()
          reader.onload = (ev) => resolve(ev.target.result)
          reader.readAsDataURL(imageFile)
        })
      }
      const newPost = await createPost(caption, imageDataUrl || null)
      onPostCreated(newPost)
    } catch {
      setError('Failed to create post. Please try again.')
    } finally {
      setCreating(false)
    }
  }

  return (
    <>
      <div className="fixed inset-0 bg-black bg-opacity-50 z-50 animate-backdrop" onClick={onClose} />
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-hidden animate-scale-in" onClick={(e) => e.stopPropagation()}>

          {/* Header */}
          <div className="flex items-center justify-between p-4 border-b border-gray-200">
            <h2 className="text-xl font-bold text-gray-900">Create New Post</h2>
            <button onClick={onClose} className="p-2 hover:bg-gray-100 rounded-full transition-colors">
              <X className="w-5 h-5 text-gray-600" />
            </button>
          </div>

          {/* Body */}
          <div className="p-6 overflow-y-auto" style={{ maxHeight: 'calc(90vh - 160px)' }}>
            {error && (
              <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-5">

              {/* User Info */}
              <div className="flex items-center space-x-3">
                <img
                  src={user?.avatar_url || "https://ui-avatars.com/api/?name=User&background=9333ea&color=fff"}
                  alt={user?.username}
                  className="w-10 h-10 rounded-full ring-2 ring-purple-100"
                />
                <div>
                  <p className="font-semibold text-gray-900">{user?.username}</p>
                  <p className="text-xs text-gray-500">Creating a post</p>
                </div>
              </div>

              {/* Caption */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Caption</label>
                <textarea
                  value={caption}
                  onChange={(e) => setCaption(e.target.value)}
                  placeholder="What's on your mind?"
                  rows={3}
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none resize-none"
                  disabled={creating}
                />
                <p className="mt-1 text-xs text-gray-500">{caption.length} characters</p>
              </div>

              {/* Hidden file input */}
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleInputChange}
                className="hidden"
              />

              {/* Upload area or Preview */}
              {!imagePreview ? (
                <div
                  onClick={() => fileInputRef.current?.click()}
                  onDrop={handleDrop}
                  onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
                  onDragLeave={() => setDragOver(false)}
                  className={`w-full flex flex-col items-center justify-center px-4 py-10 border-2 border-dashed rounded-xl cursor-pointer transition-all ${
                    dragOver
                      ? 'border-purple-500 bg-purple-50'
                      : 'border-gray-300 hover:border-purple-400 hover:bg-purple-50'
                  }`}
                >
                  <div className="w-14 h-14 bg-purple-100 rounded-full flex items-center justify-center mb-3">
                    <Upload className="w-7 h-7 text-purple-600" />
                  </div>
                  <p className="text-sm font-semibold text-gray-700">Click to upload an image</p>
                  <p className="text-xs text-gray-500 mt-1">or drag and drop here</p>
                  <p className="text-xs text-gray-400 mt-2">JPG, PNG, GIF, WebP — max 10MB</p>
                </div>
              ) : (
                <div className="relative rounded-xl overflow-hidden border border-gray-200">
                  <img
                    src={imagePreview}
                    alt="Preview"
                    className="w-full object-cover max-h-72"
                  />
                  {/* Buttons overlay */}
                  <div className="absolute top-2 right-2 flex space-x-2">
                    <button
                      type="button"
                      onClick={() => fileInputRef.current?.click()}
                      className="bg-white bg-opacity-90 hover:bg-opacity-100 text-gray-700 px-3 py-1.5 rounded-lg text-xs font-medium shadow flex items-center space-x-1 transition-all"
                    >
                      <ImageIcon className="w-3.5 h-3.5" />
                      <span>Change</span>
                    </button>
                    <button
                      type="button"
                      onClick={removeImage}
                      className="bg-red-500 hover:bg-red-600 text-white px-3 py-1.5 rounded-lg text-xs font-medium shadow flex items-center space-x-1 transition-all"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                      <span>Remove</span>
                    </button>
                  </div>
                  {/* Filename bar */}
                  <div className="bg-gray-50 px-3 py-2 border-t border-gray-200">
                    <p className="text-xs text-gray-500 truncate">📎 {imageFile?.name}</p>
                  </div>
                </div>
              )}

              {/* Tip */}
              <div className="bg-purple-50 border border-purple-100 rounded-xl p-4">
                <p className="text-xs text-purple-800">
                  <span className="font-semibold">Tip:</span> After posting, click Verify to fact-check your post automatically.
                </p>
              </div>

            </form>
          </div>

          {/* Footer */}
          <div className="p-4 border-t border-gray-200 flex items-center justify-end space-x-3">
            <button
              onClick={onClose}
              disabled={creating}
              className="px-6 py-2 border border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 transition-colors disabled:opacity-50"
            >
              Cancel
            </button>
            <button
              onClick={handleSubmit}
              disabled={!caption.trim() || creating}
              className="px-6 py-2 bg-gradient-to-r from-purple-600 to-purple-700 text-white rounded-xl hover:from-purple-700 hover:to-purple-800 transition-all shadow-md disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {creating ? (
                <span className="flex items-center">
                  <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                  Publishing...
                </span>
              ) : 'Publish Post'}
            </button>
          </div>

        </div>
      </div>
    </>
  )
}

export default CreatePostModal