class Feed < ApplicationRecord
  has_many :likes
  has_many :comments
end
